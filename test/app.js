const express = require("express");
const multer = require("multer");
var cors = require('cors')

const upload = multer({
    dest: "uploads/"
});
const app = express();
app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));
app.use(cors());


app.post("/upload_files", upload.array("files"), uploadFiles);

function uploadFiles(req, res) {
    console.log(req.body);
    console.log(req.files);
    let data = {
        0: {
            "url1": "https://scontent.fbkk22-3.fna.fbcdn.net/v/t39.30808-6/332864971_596287035680928_8265893715599890000_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_ohc=ugglE91i5VMAX_waCrX&_nc_oc=AQkpoTDr2Qh2iviRFvUQapwmwHTc0ESn7xIQCBrvQaGZ8OtVi5ERwRXUtvfIY3-3WHmBU0OTVdwhTVl7S6tbDo_9&_nc_ht=scontent.fbkk22-3.fna&oh=00_AfBk7T5KUIrVQtYbLhFDtTZnQDg-_OFoPqjbx_XmhNwMFA&oe=63FBE89B",
            "url2": "https://scontent.fbkk22-3.fna.fbcdn.net/v/t39.30808-6/332864971_596287035680928_8265893715599890000_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=730e14&_nc_ohc=ugglE91i5VMAX_waCrX&_nc_oc=AQkpoTDr2Qh2iviRFvUQapwmwHTc0ESn7xIQCBrvQaGZ8OtVi5ERwRXUtvfIY3-3WHmBU0OTVdwhTVl7S6tbDo_9&_nc_ht=scontent.fbkk22-3.fna&oh=00_AfBk7T5KUIrVQtYbLhFDtTZnQDg-_OFoPqjbx_XmhNwMFA&oe=63FBE89B",
            0: [40, 30, 20, 50],
            1: [40, 30, 20, 50],
            "name": "Pre-operative"
        },
        1: {
            "url1": "https://scontent.fbkk22-6.fna.fbcdn.net/v/t39.30808-6/332184131_1477573286155078_3032701065999842721_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=W0i5L4wjp6oAX-DY7cU&_nc_ht=scontent.fbkk22-6.fna&oh=00_AfDLUNZS8Elml09wW3mYGa-cP632uEi9L0-bNOLJ2qO3Aw&oe=63FEB63B",
            "url2": "https://scontent.fbkk22-6.fna.fbcdn.net/v/t39.30808-6/332184131_1477573286155078_3032701065999842721_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=W0i5L4wjp6oAX-DY7cU&_nc_ht=scontent.fbkk22-6.fna&oh=00_AfDLUNZS8Elml09wW3mYGa-cP632uEi9L0-bNOLJ2qO3Aw&oe=63FEB63B",
            0: [40, 30, 20, 50],
            1: [40, 30, 20, 50],
            "name": "Pre-operative and Pre-operative"
        }
    };
    res.json(data);
}

app.listen(3000, () => {
    console.log(`Server started...`);
});