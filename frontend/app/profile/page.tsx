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

            setMessage(response.data.detail);
            setOldPassword('');
            setNewPassword('');
            setConfirmPassword('');
        } catch (error) {
            setMessage(error.response.data.detail);
        }
    };

    return (
        <div>
            <h1>Change Password</h1>
            <div>
                {message && <p style={{ color: 'red' }}>{message}</p>}
                <label>Old Password:</label>
                <input
                    type="password"
                    value={oldPassword}
                    onChange={(e) => setOldPassword(e.target.value)}
                    style={{ color: 'black' }} // Set text color to black
                /><br />
                <label>New Password:</label>
                <input
                    type="password"
                    value={newPassword}
                    onChange={(e) => setNewPassword(e.target.value)}
                    style={{ color: 'black' }} // Set text color to black
                /><br />
                <label>Confirm Password:</label>
                <input
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    style={{ color: 'black' }} // Set text color to black
                /><br />
                <button onClick={handleChangePassword}>Change Password</button>
            </div>
        </div>
    );
}
