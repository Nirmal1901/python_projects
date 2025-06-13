const express = require("express");
const nodemailer = require("nodemailer");

const app = express();
const PORT = 5000;

const sendMailController = async (req, res) => {
  try {
    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: 'devnirmalnathnai@gmail.com',
        pass: 'Gmail@1901'
      }
    })

    const mailOptions = {
      from: '"Nirmal" <devnirmalnathani@gmail.com>',
      to: "mridul.nathani@gmail.com",
      subject: "Hello Gmail",
      text: "Hello",
      html: "<b>Hello</b>",
    };

    let info = await transporter.sendMail(mailOptions);

    console.log("Message sent: %s", info.messageId);
    res.json(info);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Internal Server Error" });
  }
};

app.get("/", (req, res) => {
  res.send("I am a server");
});

app.get("/mail", sendMailController);

const start = async () => {
  try {
    app.listen(PORT, () => {
      console.log(`Server is live on port no. ${PORT}`);
    });
  } catch (error) {
    console.error(error);
  }
};

start();
