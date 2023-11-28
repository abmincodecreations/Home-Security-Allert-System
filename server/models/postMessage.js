import mongoose from 'mongoose';

const postSchema = mongoose.Schema({
tittle: String,
message:String,
Creator:String,
selectedFile: String,
likeCount: {
  type: Number,
  default:new Date()
},
createdAt:{
  type: Date,
  default:new Date()
}
});

const PostMessage= mongoose.model('PostMessage', postSchema):

export default PostMessage;