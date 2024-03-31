import React, { useState, createContext, useEffect }from 'react';

import api from '../core/baseAPI';

const AuthContext = createContext();

export function AuthProvider({children}) {
    const [auth, setAuth] = useState({});
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const auth = sessionStorage.getItem('auth');
        console.log('ran')
        if (auth) {
            setAuth(JSON.parse(auth));
            setIsLoading(false);
        } else {
            api.get('accounts/user')
            .then((response) => {
                sessionStorage.setItem('auth', JSON.stringify({
                    isAuthenticated: true,
                    username: response.data.username,
                    avatar: response.data.avatar ? response.data.avatar : null
                }));
                setAuth({
                    isAuthenticated: true,
                    username: response.data.username,
                    avatar: response.data.avatar
                });
            })
            .catch((error) => {
                setAuth({
                    isAuthenticated: false,
                    username: '',
                    avatar: ''
                });
            })
            .finally(() => {
                setIsLoading(false);
            });
        }
    }, []);
    if (isLoading) {
        console.log('Loading', isLoading)
        return <div>Loading...</div>
    }

    const setIsAuthenticated = (isAuthenticated) => {
        setAuth((prevState) => {
            return {
                ...prevState,
                isAuthenticated: isAuthenticated
            }
        });
    }

    const setUsername = (username) => {
        setAuth((prevState) => {
            return {
                ...prevState,
                username: username
            }
        });
    }

    const setAvatar = (avatar) => {
        setAuth((prevState) => {
            return {
                ...prevState,
                avatar: avatar
            }
        });
    }

    return (
        <AuthContext.Provider value={{ auth, setIsAuthenticated, setUsername, setAvatar }}>
            {children}
        </AuthContext.Provider>
    )
}


export default AuthContext;