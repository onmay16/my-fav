import axios from 'axios'

const fetcher = async (method, url, ...rest) => {
    axios.defaults.baseURL = 'http://localhost:8000';
    axios.defaults.withCredentials = true;
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';
    axios.defaults.xsrfCookieName = 'csrftoken';

    // const headers = {
    //   'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    //   'Accept': '*/*',
    //   'Access-Control-Allow-Origin': '*',
    //   'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS'
    // }

    try {
        const res = await axios[method](url, ...rest);
        return res.data;
    } catch (err) {
        return err.response;
        //
    }
};

export default fetcher;