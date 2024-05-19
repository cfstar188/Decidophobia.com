import React, { useState, createContext, useEffect } from 'react';
import api from '../core/baseAPI';

const AuthContext = createContext();

export function AuthProvider({ children }) {
    const [auth, setAuth] = useState({});
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const storedAuth = sessionStorage.getItem('auth');
        if (storedAuth) {
            setAuth(JSON.parse(storedAuth));
            setIsLoading(false);
        } else {
            api.get('accounts/user')
                .then((response) => {
                    const userData = {
                        isAuthenticated: true,
                        username: response.data.username,
                        email: response.data.email,
                        full_name: response.data.full_name,
                        avatar: response.data.avatar ? response.data.avatar : null,
                    };
                    sessionStorage.setItem('auth', JSON.stringify(userData));
                    setAuth(userData);
                })
                .catch((error) => {
                    console.error('Failed to fetch user data:', error);
                    setAuth({
                        isAuthenticated: false,
                        username: '',
                        email: '',
                        full_name: '',
                        avatar: '',
                    });
                })
                .finally(() => {
                    setIsLoading(false);
                });
        }
    }, []);

    if (isLoading) {
        return <div>Loading...</div>;
    }

    const setIsAuthenticated = (isAuthenticated) => {
        setAuth((prevState) => ({
            ...prevState,
            isAuthenticated,
        }));
    };

    const setUsername = (username) => {
        setAuth((prevState) => ({
            ...prevState,
            username,
        }));
    };

    const setEmail = (email) => {
    setAuth((prevState) => ({
        ...prevState,
        email,
    }));
    localStorage.setItem('currentEmail', email); // Update email in local storage
    };

    const setName = (full_name) => {
        setAuth((prevState) => ({
            ...prevState,
            full_name,
        }));
    };

    const setAvatar = (avatar) => {
        setAuth((prevState) => ({
            ...prevState,
            avatar,
        }));
    };

    return (
        <AuthContext.Provider value={{ auth, setIsAuthenticated, setUsername, setEmail, setName, setAvatar }}>
            {children}
        </AuthContext.Provider>
    );
}

export default AuthContext;
