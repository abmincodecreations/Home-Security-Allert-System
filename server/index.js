import express from 'express';
import bodyParser from 'body-parser';
import mongoose from 'mongoose';
import cors from 'cors';
import postRoutes from './routes/posts.js'
import bcrypt from 'bcrypt'
import jwt from 'jsonwebtoken';

const app = express();

app.use(express.json());
app.use(cors());
app.use(express.json());

const users = [];

app.use('/posts' , postRoutes);
app.use(bodyParser.json({ limit: "30mb" , extended: true}));
app.use(bodyParser.urlencoded({ limit: "30mb" , extended: true}));
app.use(cors());
const CONNECTION_URL='mongodb+srv://homesecura:homesecura123code48@clusterhomesecura.fpnletf.mongodb.net/?retryWrites=true&w=majority';
const PORT= process.env.PORT || 5000;
// remeber to create envaronmental variable


mongoose.connect(CONNECTION_URL,{useNewUrlParser: true , useUnifiedTopology:true})
.then(()=>app.listen( PORT, ()=> console.log(`server running on port:${PORT}`)))
.catch((error)=>console.log(error.message));


mongoose.set('useFindAndModify', false);






