'use client'

import React, { useState, useEffect } from 'react';
import AuthContext from "@/app/contexts/AuthContext";

export function AuthProvider({ children }: { children: React.ReactNode }) {

  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [username, setUsername] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      setIsAuthenticated(true);
      setUsername('User'); // Replace 'User' with the actual username
    }
  }, []);

  return (
    <AuthContext.Provider value={{
        isAuthenticated: isAuthenticated,
        username: username 
      }}>
      {children}
    </AuthContext.Provider>
  );
}