// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAd-qNqH8eXrUSddKUFrvOa5qkFn2D2dPM",
  authDomain: "proto-llm-49f38.firebaseapp.com",
  projectId: "proto-llm-49f38",
  storageBucket: "proto-llm-49f38.appspot.com",
  messagingSenderId: "265053902228",
  appId: "1:265053902228:web:fd45c78503533a1161ab81",
  measurementId: "G-KK637JDKJ3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);