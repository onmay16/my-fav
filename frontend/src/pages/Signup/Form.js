import React from 'react';
import './Form.css'

function Form(text) {
    return (
            <form action="">
                <label htmlFor={text}>{text}</label>
                <br />
                <input type='text' id={text} name={text} />
            </form>
    );
}

export default Form;
