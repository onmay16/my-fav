import React from 'react'

import './PostDetail.css'

import hamster from '../../image/VhamsterV.jpg'

import detailPlus from '../../svg/detail-plus.svg'
import detailEdit from '../../svg/detail-edit.svg'
import detailDelete from '../../svg/detail-delete.svg'
import detailClose from '../../svg/detail-close.svg'
import axios from 'axios'

const PostDetail = (props) => {

    const detailShowHide = props.detailModal ? "post-detail-bg display-block" : "post-detail-bg display-none";
    const postInfo = props.postInfo;
    const postImg = props.postImg;
    const nickname = props.nickname;
    const postId = postInfo.id;

    function closeModal() {
        props.setDetailModal(false);
    }

    // console.log(props.postInfo);

    function postEdit() {
    
        axios.post("http://ec2-54-81-90-22.compute-1.amazonaws.com/playlist/" + postId + "/edit/", {
        // axios.post("http://localhost:8000/playlist/" + postId + "/edit/", {

        })
    }

    function postDelete() {

        if (window.confirm("Are you sure you want to delete this post?") == true) {
            
            axios.get("http://ec2-54-81-90-22.compute-1.amazonaws.com/playlist/post/" + postId + "/delete/")
            // axios.get("http://localhost:8000/playlist/post/" + postId + "/delete/")
            .then(function (response) {
                // console.log(response);
                alert(response.data.message);
                // close post detail page and rerender the feed
                window.location.reload();
            }).catch(function (error) {
                console.log(error);
            })
        }
    }

    return (
        <div className={detailShowHide}>
            <div className="enitre-post-detail">
                <div className="post-section">
                    <img src={postImg} alt="" className="detail-cover-image" />
                    <div className="post-content">
                        <span className="post-owner">{nickname}</span>
                        <span className="post-description">{postInfo.content}</span>
                    </div>
                    <img src={detailPlus} alt="" className="detail-plus" />
                </div>
                <div className="comment-section">
                    <img src={detailClose} alt="" className="detail-close" onClick={closeModal}/>
                    {/* onClick={() => setDetailVisible(false)} */}
                    <div className="comment-user cu1">
                        <img src={hamster} alt="" className="cu-profile-pic cmp1" />
                        <span className="cu-id cui1">VhamsterV</span>
                        <span className="cu-comment cuc1">i love this song too! 🎶</span>
                    </div>
                    <div className="ed-buttons">
                        <img src={detailEdit} alt="" className='detail-edit'/>
                        <img src={detailDelete} alt="" className="detail-delete" onClick={postDelete}/>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default PostDetail

