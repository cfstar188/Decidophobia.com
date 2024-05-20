'use client'
import React, { useState, useContext, useEffect } from "react";
import api from "../core/baseAPI";
import AuthContext from "../contexts/AuthContext";
import styles from './SettingsPage.module.css';

interface SettingsPageProps {}

const SettingsPage: React.FC<SettingsPageProps> = () => {
  const { auth } = useContext(AuthContext);
  const [isChangePasswordModalOpen, setIsChangePasswordModalOpen] = useState(false);
  const [isChangeEmailModalOpen, setIsChangeEmailModalOpen] = useState(false);
  const [isChangeProfilePictureModalOpen, setIsChangeProfilePictureModalOpen] = useState(false);
  const [message, setMessage] = useState('');
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [password, setPassword] = useState('');
  const [newEmail, setNewEmail] = useState('');
  const [currentEmail, setCurrentEmail] = useState(auth.email);
  const [profilePicture, setProfilePicture] = useState<File | null>(null);

  const title = "Edit Details";

  const handleOpenChangePasswordModal = () => {
    setIsChangePasswordModalOpen(true);
  };

  const handleCloseChangePasswordModal = () => {
    setIsChangePasswordModalOpen(false);
    setMessage('');
  };

  const handleOpenChangeEmailModal = () => {
    setIsChangeEmailModalOpen(true);
  };

  const handleCloseChangeEmailModal = () => {
    setIsChangeEmailModalOpen(false);
    setPassword('');
    setNewEmail('');
    setMessage('');
  };

  const handleOpenChangeProfilePictureModal = () => {
    setIsChangeProfilePictureModalOpen(true);
  };

  const handleCloseChangeProfilePictureModal = () => {
    setIsChangeProfilePictureModalOpen(false);
    setProfilePicture(null);
    setMessage('');
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

  const handleChangeEmail = async () => {
    try {
      const requestData = {
        password: password,
        new_email: newEmail,
      };

      const response = await api.put('accounts/change-email/', requestData);
      setMessage('Email changed successfully!');
      setPassword('');
      setCurrentEmail(newEmail); // Update currentEmail state directly
    } catch (error) {
      if (error.response && error.response.status === 400 && error.response.data && error.response.data.detail) {
        setMessage(error.response.data.detail);
      } else if (error.response && error.response.status === 400 && error.response.data && error.response.data.password) {
        setMessage('Password is incorrect');
      } else {
        setMessage('An error occurred while changing the email.');
      }
    }
  };

  const handleProfilePictureChange = async () => {
    try {
      if (!profilePicture) {
        setMessage('Please choose a valid file');
        return;
      }

      const formData = new FormData();
      formData.append('profile_picture', profilePicture);

      const response = await api.put('accounts/change-profile-picture/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setMessage('Profile picture changed successfully!');
      setProfilePicture(null);
    } catch (error) {
      if (error.response) {
        if (error.response.status === 400) {
          if (error.response.data.profile_picture) {
            setMessage('Error with profile picture: ' + error.response.data.profile_picture.join(' '));
          } else if (error.response.data.detail) {
            setMessage(error.response.data.detail);
          } else {
            setMessage('An error occurred while changing the profile picture.');
          }
        } else {
          setMessage('An error occurred: ' + error.response.statusText);
        }
      } else {
        setMessage('An error occurred while changing the profile picture.');
      }
    }
  };

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Enter') {
        if (isChangePasswordModalOpen) {
          handleChangePassword();
        } else if (isChangeEmailModalOpen) {
          handleChangeEmail();
        } else if (isChangeProfilePictureModalOpen) {
          handleProfilePictureChange();
        }
      } else if (event.key === 'Escape') {
        if (isChangePasswordModalOpen) {
          handleCloseChangePasswordModal();
        } else if (isChangeEmailModalOpen) {
          handleCloseChangeEmailModal();
        } else if (isChangeProfilePictureModalOpen) {
          handleCloseChangeProfilePictureModal();
        }
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, [isChangePasswordModalOpen, isChangeEmailModalOpen, isChangeProfilePictureModalOpen, oldPassword, newPassword, confirmPassword, password, newEmail, profilePicture]);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>{title}</h1>
      <div>
        {/* Settings options */}
        <button className={styles.button} onClick={handleOpenChangePasswordModal}>Change Password</button>
        <button className={styles.button} onClick={handleOpenChangeEmailModal}>Change Email</button>
        <button className={styles.button} onClick={handleOpenChangeProfilePictureModal}>Change Profile Picture</button>
      </div>

      {/* Change Password Modal */}
      <div className={`${styles.modalOverlay} ${isChangePasswordModalOpen ? styles.open : ''}`}>
        <div className={`${styles.modalContent} ${isChangePasswordModalOpen ? styles.open : ''}`}>
          <h2 className={styles.modalTitle}>Change Password</h2>
          <div>
            {message && message === 'Passwords do not match' && <p className={styles.modalErrorMessage}>{message}</p>}
            {message && message === 'Old password is incorrect' && <p className={styles.modalErrorMessage}>{message}</p>}
            {message && message !== 'Passwords do not match' && message !== 'Old password is incorrect' && <p className={styles.modalMessage}>{message}</p>}
            <label className={styles.label}>Old Password</label>
            <input className={styles.input} type="password" value={oldPassword} onChange={(e) => setOldPassword(e.target.value)} />
            <label className={styles.label}>New Password</label>
            <input className={styles.input} type="password" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} />
            <label className={styles.label}>Confirm New Password</label>
            <input className={styles.input} type="password" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
            <button className={styles.changeButton} onClick={handleChangePassword}>Change Password</button>
            <button className={styles.closeButton} onClick={handleCloseChangePasswordModal}>Close</button>
          </div>
        </div>
      </div>

      {/* Change Email Modal */}
      <div className={`${styles.modalOverlay} ${isChangeEmailModalOpen ? styles.open : ''}`}>
        <div className={`${styles.modalContent} ${isChangeEmailModalOpen ? styles.open : ''}`}>
          <h2 className={styles.modalTitle}>Change Email</h2>
          <div>
            {message && message === 'Password is incorrect' && <p className={styles.modalErrorMessage}>{message}</p>}
            {message && message !== 'Password is incorrect' && <p className={styles.modalMessage}>{message}</p>}
            <label className={styles.label}>Current Email: {currentEmail}</label>
            <label className={styles.label}>Password</label>
            <input className={styles.input} type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <label className={styles.label}>New Email</label>
            <input className={styles.input} type="email" value={newEmail} onChange={(e) => setNewEmail(e.target.value)} />
            <button className={styles.changeButton} onClick={handleChangeEmail}>Change Email</button>
            <button className={styles.closeButton} onClick={handleCloseChangeEmailModal}>Close</button>
          </div>
        </div>
      </div>

      {/* Change Profile Picture Modal */}
      <div className={`${styles.modalOverlay} ${isChangeProfilePictureModalOpen ? styles.open : ''}`}>
        <div className={`${styles.modalContent} ${isChangeProfilePictureModalOpen ? styles.open : ''}`}>
          <h2 className={styles.modalTitle}>Change Profile Picture</h2>
          <div>
            {message && (
              <p className={message === 'Please choose a valid file' ? `${styles.modalErrorMessage}` : `${styles.modalErrorMessage}`}>
                {message === 'Please choose a valid file' ? message : (
                  <span className={styles.modalMessage}>{message}</span>
                )}
              </p>
            )}
            <label className={styles.label}>Upload New Profile Picture</label>
            <input className={styles.input} type="file" accept="image/*" onChange={(e) => setProfilePicture(e.target.files[0])} />
            <button className={styles.changeButton} onClick={handleProfilePictureChange}>Change Profile Picture</button>
            <button className={styles.closeButton} onClick={handleCloseChangeProfilePictureModal}>Close</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SettingsPage;
