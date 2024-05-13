'use client'
import React, { useState } from "react";
import { useClient } from 'next/client'; // Import useClient
import api from "../core/baseAPI";

interface SettingsPageProps {}

const SettingsPage: React.FC<SettingsPageProps> = () => {
  const [isChangePasswordModalOpen, setIsChangePasswordModalOpen] = useState(false);
  const [message, setMessage] = useState('');
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const title = "Edit Details";

  const handleOpenChangePasswordModal = () => {
    setIsChangePasswordModalOpen(true);
  };

  const handleCloseChangePasswordModal = () => {
    setIsChangePasswordModalOpen(false);
  };

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
    if (error.response && error.response.status === 400 && error.response.data && error.response.data.detail) {
      setMessage(error.response.data.detail);
    } else if (error.response && error.response.status === 400 && error.response.data && error.response.data.old_password) {
      setMessage('Old password is incorrect');
    } else {
      setMessage('An error occurred while changing the password.');
    }
  }
};


  return (
    <div style={{ width: '600px', margin: '100px auto', padding: '40px', border: '2px solid #ccc', borderRadius: '12px', backgroundColor: '#f9f9f9', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.2)' }}>
      <h1 style={{ textAlign: 'center', color: 'black', fontWeight: 'bold', fontSize: '32px', marginBottom: '30px' }}>{title}</h1>
      <div style={{ marginTop: '30px' }}>
        {/* Settings options */}
        <button style={{ width: '100%', padding: '16px', fontSize: '18px', backgroundColor: '#2E8BC0', color: 'white', border: 'none', borderRadius: '8px', cursor: 'pointer', transition: 'background-color 0.3s', marginBottom: '20px' }} onClick={handleOpenChangePasswordModal}>Change Password</button>
        {/* Other buttons */}
      </div>

   {/* Change Password Modal */}
{isChangePasswordModalOpen && (
  <div style={{ position: 'fixed', top: 0, left: 0, width: '100%', height: '100%', backgroundColor: 'rgba(0, 0, 0, 0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
    <div style={{ background: '#fff', padding: '40px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0, 0, 0, 0.2)', width: '60%', maxWidth: '800px' }}>
      <h2 style={{ textAlign: 'center', color: 'black', fontWeight: 'bold', fontSize: '24px', marginBottom: '20px' }}>Change Password</h2>
      <div style={{ marginTop: '20px' }}>
        {message && message === 'Passwords do not match' && <p style={{ color: 'red', marginBottom: '10px', textAlign: 'center', fontSize: '18px' }}>{message}</p>}
        {message && message === 'Old password is incorrect' && <p style={{ color: 'red', marginBottom: '10px', textAlign: 'center', fontSize: '18px' }}>{message}</p>}
        {message && message !== 'Passwords do not match' && message !== 'Old password is incorrect' && <p style={{ color: 'green', marginBottom: '10px', textAlign: 'center', fontSize: '18px' }}>{message}</p>}
        <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold', color: 'black', fontSize: '18px' }}>Old Password:</label>
        <input
          type="password"
          value={oldPassword}
          onChange={(e) => setOldPassword(e.target.value)}
          style={{ width: '100%', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '6px', color: 'black', fontSize: '18px' }}
        /><br />
        <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold', color: 'black', fontSize: '18px' }}>New Password:</label>
        <input
          type="password"
          value={newPassword}
          onChange={(e) => setNewPassword(e.target.value)}
          style={{ width: '100%', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '6px', color: 'black', fontSize: '18px' }}
        /><br />
        <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold', color: 'black', fontSize: '18px' }}>Confirm Password:</label>
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          style={{ width: '100%', padding: '10px', marginBottom: '20px', border: '1px solid #ccc', borderRadius: '6px', color: 'black', fontSize: '18px' }}
        /><br />
        <button onClick={handleChangePassword} style={{ width: '100%', padding: '12px', backgroundColor: '#2E8BC0', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', transition: 'background-color 0.3s', fontSize: '18px' }}>Change Password</button>
      </div>

      <button onClick={handleCloseChangePasswordModal} style={{ float: 'right', marginTop: '10px', padding: '8px 16px', backgroundColor: '#ccc', color: 'black', border: 'none', borderRadius: '4px', cursor: 'pointer', fontSize: '18px' }}>Close</button>
    </div>
  </div>
)}

    </div>
  );
};

export default SettingsPage;
