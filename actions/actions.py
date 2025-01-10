# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
import re

class ActionLookupEnglish(Action):
    def name(self) -> Text:
        return "action_lookUp_en"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        word = str(tracker.get_slot('enword')).lower()
        print(word)

        if not word:
            dispatcher.utter_message("😴Zzzzzz... Tôi ngủ rồi, hãy đánh thức tôi khi bạn cần!")
            return []

        url = 'https://api.tracau.vn/WBBcwnwQpV89/s/{}/en'.format(word)

        try:
            # Request to API
            response = requests.get(url)
            response.raise_for_status()  # Will raise an HTTPError if status is not 200

            # Parse response as JSON
            json_data = response.json()
            # Extract data from the JSON response
            json_data = json_data.get('tratu', [{}])[0].get('fields', {}).get('fulltext', '')

            # Search for word properties and meaning using regex
            try:
                pro = re.search(r"<\s*tr\s+id\s*=\s*\"pa\"[^>]*>.+?<\s*\/\s*tr>", json_data).group()
                tl = re.search(r"<\s*tr\s+id\s*=\s*\"tl\"[^>]*>.+?<\s*\/\s*tr>", json_data).group()
            except Exception as e1:
                print(f"Error extracting properties (pro/tl): {e1}")
                pro, tl = None, None

            # Extract meanings
            try:
                meanings = re.findall(r"<\s*tr\s+id\s*=\s*\"mn\"[^>]*>.+?<\s*\/\s*tr>", json_data)
            except Exception as e2:
                print(f"Error extracting meanings: {e2}")
                dispatcher.utter_message("😴Zzzzzz... Tôi ngủ rồi, hãy đánh thức tôi khi bạn cần!")
                return []

            # Clean up the data (remove HTML tags)
            pro = re.sub(r"<\s*[^>]+>", "", pro) if pro else ''
            tl = re.sub(r"<\s*[^>]+>", "", tl) if tl else ''
            for i in range(len(meanings)):
                meanings[i] = re.sub(r"<\s*[^>]+>", "", meanings[i])

            # Build response
            text_respond = "=> " + word.title()
            if pro:
                text_respond += pro.replace("◘", " ")
            if tl:
                text_respond += "\n" + tl.replace("*", "* ")
            if meanings:
                for mean in meanings:
                    if mean:
                        text_respond += "\n" + mean.replace("■", "  -  ")

                dispatcher.utter_message("✅💯😼 Bằng sự thông minh của tôi 🗣 đây là thông tin về từ '{}' mà bạn cần:\n".format(word) + text_respond)
            else:
                dispatcher.utter_message("😴Zzzzzz... Tôi ngủ rồi, hãy đánh thức tôi khi bạn cần!")
                return []

        except Exception as e:
            # Handle other general errors
            print(f"Unexpected error: {e}")
            dispatcher.utter_message("😴Zzzzzz... Tôi ngủ rồi, hãy đánh thức tôi khi bạn cần!")

        return []
