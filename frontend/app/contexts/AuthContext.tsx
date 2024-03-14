'use client'

import React from 'react';

const AuthContext = React.createContext({
    isAuthenticated: false,
    username: ''
  });

export default AuthContext;