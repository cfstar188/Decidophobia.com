// localhost:3000/login
'use client'

import React, { useState } from 'react';
import api from '../core/baseAPI';

import { Button } from 'reactstrap';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleUsernameChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: { target: { value: React.SetStateAction<string>; }; }) => {
    setPassword(event.target.value);
  };

  const handleSubmit = (data: React.FormEvent<HTMLFormElement>) => {
    data.preventDefault();
    console.log('Username:', username);
    console.log('Password:', password);

    api.post('/login/', {
      username: username,
      password: password
    }, {
      headers: {"Content-Type": "application/json"},
    })
    .then((response: any) => {
      console.log(response.data);
      localStorage.setItem('token', JSON.stringify(response.data));
      window.location.href = '/';
    })
    .catch((error: any) => {
      setError("Invalid login!")
    });
  };

  return (
    <>
      <p className="text-center m-auto">Login</p>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" value={username} onChange={handleUsernameChange} style={{ color: 'black', marginLeft: '0.5rem' }}/>
        </label>
        <br />
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={handlePasswordChange} style={{ color: 'black', marginLeft: '0.5rem' }}/>
        </label>
        <br />
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <Button type="submit">Login</Button>
      </form>
    </>
  );
}