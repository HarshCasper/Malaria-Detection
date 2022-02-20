# Detecting Malaria using Deep Learning 🦟🦠

<p align="center">
  <a href="https://github.com/HarshCasper/Malaria-Detection">
    <img src="https://pngimage.net/wp-content/uploads/2018/06/malaria-in-png-1.png" alt="Logo" width="150" height="150">
  </a>

## 📌 Introduction

This Machine Learning Web Application utilizes a Two-Layered Convolutional Neural Network to process the Cell Images and predict if they are Malarial with an accuracy of nearly 95%. The [Dataset](https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria) to process the Deep Learning Algorithm is taken from the official US National Library of Medicine's NIH Website which is a repository of segmented cells from the thin blood smear slide images from the Malaria Screener research activity.

## 🎯 Purpose of the Project

Where malaria is not endemic any more (such as in the United States), health-care providers may not be familiar with the disease. Clinicians seeing a malaria patient may forget to consider malaria among the potential diagnoses and not order the needed diagnostic tests. Laboratorians may lack experience with malaria and fail to detect parasites when examining blood smears under the microscope. Malaria is an acute febrile illness. 

In a non-immune individual, symptoms usually appear 10–15 days after the infective mosquito bite. The first symptoms – fever, headache, and chills – may be mild and difficult to recognize as malaria. If not treated within 24 hours, P. falciparum malaria can progress to severe illness, often leading to death. 

Our Model performs fairly well with an accuracy of 95% and an F1 Score of 95% and Recall Score of 92%. This provides a handy tool to utilize the power of Machine Learning and Artificial Intelligence in Binary Classification Problems where time and accuracy is the paramount objective of classification.

## 🏁 Technology Stack

* [Flask](https://github.com/pallets/flask)
* [HTML](https://www.w3.org/TR/html52/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Bootstrap](https://getbootstrap.com/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](http://keras.io/)

## 🏃‍♂️ Local Installation

1. Drop a ⭐ on the Github Repository. 
2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
git clone https://github.com/HarshCasper/Malaria-Detection.git
```

3. Install the Packages: 
```sh
pip install -r requirements.txt
```

4. At last, push in the command:
```sh
python app.py
```

5. Go to ` http://127.0.0.1:5000/` and enjoy the application.

## 📋 Further Changes to be Done

- [ ] Deploying the Web Application on Cloud.
- [ ] Development of an architecture using Pre-Trained Model like VGG16.
- [ ] Implementing the Model in PyTorch.
- [ ] Enhance the User-Interface using HTML/CSS.
- [ ] Set the Application on Docker.

## 📜 LICENSE

[MIT](https://github.com/HarshCasper/Malaria-Detection/blob/master/LICENSE)
