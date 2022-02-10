import React, { useState } from 'react';
import './Form.css'

function Form(props) {

    return (
        <form>
            <label htmlFor={props.text}>{props.text}</label>
            <br />
            <input type={props.type} id={props.text} name={props.text} value={props.value} onChange={props.onChange} />
        </form>
    );
}

export default Form;
