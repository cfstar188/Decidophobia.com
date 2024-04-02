import axios from 'axios';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
axios.defaults.withCredentials = true;
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
});

api.interceptors.request.use(
    config => {
        const token = localStorage.getItem('token');
        if (token) {
            let accessToken = JSON.parse(token)['access']
            config.headers['Authorization'] = 'Bearer ' + accessToken;
        }

        return config;
    },
    error => {
        Promise.reject(error)
    }
    )

export default api;