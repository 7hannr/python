// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCqGWmaCsubYohJC9S-Nviux1_uxpsQGXw",
  authDomain: "kosmo-c6aa8.firebaseapp.com",
  databaseURL: "https://kosmo-c6aa8-default-rtdb.firebaseio.com",
  projectId: "kosmo-c6aa8",
  storageBucket: "kosmo-c6aa8.appspot.com",
  messagingSenderId: "370681159705",
  appId: "1:370681159705:web:7ac62cdbe64b9bc3ab8a88"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);