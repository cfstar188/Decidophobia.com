<<<<<<< HEAD
import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
});


api.interceptors.request.use(
    config => {
        config.withCredentials = true;
        return config;
    },
    error => {
        Promise.reject(error)
    }
    )

=======
import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true; 
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
});

api.interceptors.request.use(
    config => {
        // config.withCredentials = true;
        return config;
    },
    error => {
        Promise.reject(error)
    }
    )

>>>>>>> main
export default api;