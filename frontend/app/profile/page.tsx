'use client'
import React, { useState } from "react";
import { useClient } from 'next/client'; // Import useClient
import api from "../core/baseAPI";

export default function ProfilePage() {
    const [message, setMessage] = useState('');
    const [username, setUsername] = useState('');
    const [oldPassword, setOldPassword] = useState('');
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const handleChangePassword = async () => {
        try {
            if (newPassword !== confirmPassword) {
                setMessage('Passwords do not match');
                return;
            }

            const requestData = {
                old_password: oldPassword,
                password: newPassword,
                password2: confirmPassword,
            };

            const response = await api.put('accounts/change-password/', requestData);

            setMessage('Password changed successfully!');
            setOldPassword('');
            setNewPassword('');
            setConfirmPassword('');
        } catch (error) {
            if (error.response.status === 400 && error.response.data.old_password) {
                setMessage('Old password is incorrect');
            } else {
                setMessage(error.response.data.detail);
            }
        }
    };

    return (
        <div style={{ width: '500px', margin: '50px auto', padding: '30px', border: '1px solid #ccc', borderRadius: '8px', backgroundColor: '#f9f9f9', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)' }}>
            <h1 style={{ textAlign: 'center', color: 'black', fontWeight: 'bold', fontSize: '24px', marginBottom: '20px' }}>Change Password</h1>
            <div style={{ marginTop: '20px' }}>
                {message && message === 'Passwords do not match' && <p style={{ color: 'red', marginBottom: '10px', textAlign: 'center' }}>{message}</p>}
                {message && message === 'Old password is incorrect' && <p style={{ color: 'red', marginBottom: '10px', textAlign: 'center' }}>{message}</p>}
                {message && message !== 'Passwords do not match' && message !== 'Old password is incorrect' && <p style={{ color: 'green', marginBottom: '10px', textAlign: 'center' }}>{message}</p>}
                <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold', color: 'black' }}>Old Password:</label>
                <input
                    type="password"
                    value={oldPassword}
                    onChange={(e) => setOldPassword(e.target.value)}
                    style={{ width: '100%', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '6px', color: 'black' }}
                /><br />
                <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold', color: 'black' }}>New Password:</label>
                <input
                    type="password"
                    value={newPassword}
                    onChange={(e) => setNewPassword(e.target.value)}
                    style={{ width: '100%', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '6px', color: 'black' }}
                /><br />
                <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold', color: 'black' }}>Confirm Password:</label>
                <input
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    style={{ width: '100%', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '6px', color: 'black' }}
                /><br />
                <button onClick={handleChangePassword} style={{ width: '100%', padding: '12px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', transition: 'background-color 0.3s' }}>Change Password</button>
            </div>
        </div>
    );
}
