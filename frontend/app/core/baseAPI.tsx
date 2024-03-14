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

export default api;