import React, {useState, useCallback} from 'react'
import axios from 'axios'
import './style.css'

function MainPage(){

    // HTTP POST request function
    const [shortenedURL, setShortenedURL] = useState("")
    const [textValue, setTextValue] = useState("")
    const handleClick = useCallback(
        () => {
            console.log(textValue)
        },
        [textValue],
    )
    
    const sendURLData = (str) => {
        console.log('sending data', str)
        axios.post('http://localhost:8000/encode', {
            params: {
                "url_string": str
            }
        }).then((response) => {
            if (response.data)
            {
                setShortenedURL("")
            }
            console.log('received ', response.data)
            setShortenedURL(response.data)

        })
        setTextValue("")
    }
    

    return(
        <div className="banner">
            <div className = "content">
                <h1>URL SHORTENER</h1>
                <p>Snap long URLs into bite size ones</p>
                <input onChange={(e) => {setTextValue(e.target.value)}} placeholder="Insert URL here..." type="text" className="urlfield" value ={textValue}/>
                <button type="button" onClick={() => {sendURLData(textValue)}}><span></span>CONVERT</button>
                {shortenedURL !== "" && <button onClick={() =>  navigator.clipboard.writeText(shortenedURL)}>{shortenedURL}</button>}
            </div>
        </div>
    );
}

export default MainPage;