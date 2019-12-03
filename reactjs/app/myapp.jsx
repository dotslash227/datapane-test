import React from 'react';
import ReactDOM from 'react-dom';

function Demo(){
    return <h1>Hello World</h1>;
}

const element = <Demo />;

ReactDOM.render(element, document.getElementById('myapp'))