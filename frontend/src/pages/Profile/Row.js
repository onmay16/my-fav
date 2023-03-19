import React, { useRef, useEffect } from 'react'
import SingleFeed from './SingleFeed';

function Row(row, songArray, postArray, openDetailModal) {

  // console.log(row)
  // console.log(songArray);
  // console.log(postArray);

  const className = 'row row' + row;
  const subSongArray = songArray.slice(row*4, row + 4);
  const subPostArray = postArray.slice(row*4, row + 4);
  
  return (
    <div className={className}>
      {subSongArray.map((song, index) => SingleFeed((row*4+index), song, subPostArray[index], openDetailModal))}
    </div>
  )
}

export default Row