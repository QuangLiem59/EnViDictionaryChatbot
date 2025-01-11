var $messages = $(".messages-content"),
  d,
  h,
  m,
  i = 0;

$(document).ready(function () {
  $messages.mCustomScrollbar();
  setTimeout(function () {
    fakeMessage();
  }, 100);
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar("scrollTo", "bottom", {
    scrollInertia: 10,
    timeout: 0,
  });
}

function setDate() {
  d = new Date();
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ":" + m + "</div>").appendTo(
      $(".message:last")
    );
  }
}

function insertMessage() {
  const msg = $(".message-input").val(); // Get the input value
  if ($.trim(msg) == "") {
    return false; // Do nothing if the message is empty
  }

  // Add user's message to the chat
  $('<div class="message message-personal">' + msg + "</div>")
    .appendTo($(".mCSB_container"))
    .addClass("new");
  setDate();
  $(".message-input").val(null); // Clear the input field
  updateScrollbar();

  // Pass the message to fakeMessage
  setTimeout(function () {
    fakeMessage(msg); // Pass the message as a parameter
  }, 1000 + Math.random() * 20 * 100);
}

// On button click, send the message
$(".message-submit").click(function () {
  insertMessage();
});

$(window).on("keydown", function (e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
});

// Update fakeMessage to accept the user message
function fakeMessage(userMessage) {
  if (!userMessage || userMessage.trim() === "") {
    console.error("Tin nhắn rỗng");
    return false; // End the function if the message is empty
  }

  console.log("Tin nhắn người dùng:", userMessage);

  // Show "typing..." message
  $(
    '<div class="message loading new"><figure class="avatar"><img src="https://cdn-icons-png.flaticon.com/512/13330/13330989.png" /></figure><span></span></div>'
  ).appendTo($(".mCSB_container"));
  updateScrollbar();

  // Simulate Rasa response after a delay
  setTimeout(function () {
    $(".message.loading").remove();

    // Send the user's message to the Rasa server
    $.ajax({
      url: "http://localhost:5005/webhooks/rest/webhook",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify({
        sender: "user123",
        message: userMessage, // Send the correct user message
      }),
      success: function (response) {
        console.log("Phản hồi từ Rasa:", response);

        // Display Rasa's response
        response.forEach((res) => {
          $(
            '<div class="message new" style="white-space: pre-line"><figure class="avatar"><img src="https://cdn-icons-png.flaticon.com/512/11306/11306137.png" /></figure>' +
              res.text +
              "</div>"
          )
            .appendTo($(".mCSB_container"))
            .addClass("new");
        });
        updateScrollbar();
      },
      error: function () {
        // Handle error
        $(
          '<div class="message new"><figure class="avatar"><img src="https://cdn-icons-png.flaticon.com/512/11306/11306137.png" /></figure>Sorry, there was an error.</div>'
        )
          .appendTo($(".mCSB_container"))
          .addClass("new");
        updateScrollbar();
      },
    });
  }, 1000);
}
