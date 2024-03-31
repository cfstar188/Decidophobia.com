import { useAtom } from 'jotai';
import React, { useEffect, useState, useContext } from 'react';
import { useRouter } from 'next/navigation' // corrected from 'next/navigation'
import { Button, Box, Modal, TextField, Typography, Divider } from '@mui/material';
import { IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import Fade from '@mui/material/Fade';
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import InputAdornment from '@mui/material/InputAdornment';

import AuthContext from '../contexts/AuthContext';
import axios from 'axios';

interface LoginModalProps {
  isOpen: boolean;
  onClose: () => void;
  setIsRegisterModalOpen: (value: boolean) => void;
}

export default function LoginModal({ isOpen, onClose, setIsRegisterModalOpen }: LoginModalProps) {
  const router = useRouter()
  const [usernameField, setUsernameField] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  // const [auth, setAuth] = useAtom(authAtom);
  const [showPassword, setShowPassword] = useState(false);
  const { auth, setIsAuthenticated, setUsername, setAvatar} = useContext(AuthContext);

  const style = {
    position: 'absolute' as 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

  const openRegisterModal = () => {
    handleClose();
    setIsRegisterModalOpen(true);
  }
  const handleClose = () => {
    setUsernameField('');
    setPassword('');
    setError('');
    onClose();
  }

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsernameField(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  useEffect(() => {
    console.log('auth', auth);
  }, [auth]);

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    axios.defaults.withCredentials = true;
    const api = axios.create();

    api.post('http://127.0.0.1:8000/accounts/login/', {
      username: usernameField,
      password: password
    }, {
      headers: {"Content-Type": "application/json"},
    })
    .then((response: any) => {
      localStorage.setItem('token', JSON.stringify({
        access: response.data.access,
        refresh: response.data.refresh
      }));
      setIsAuthenticated(true);
      setUsername(response.data.username);
      setAvatar(response.data.avatar ? response.data.avatar : null);
      sessionStorage.setItem('auth', JSON.stringify({
        isAuthenticated: true,
        username: response.data.username,
        avatar: response.data.avatar ? response.data.avatar : null
      }))
      handleClose();
      router.push('/');
    })
    .catch((error: any) => {
      console.log(error);
      setError("Invalid login!")
    });
  };

  return (
    <>
    <Modal
        open={isOpen}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
    >
      <Fade in={isOpen}>
        <Box sx={style}>
          <IconButton
            aria-label="close"
            onClick={handleClose}
            sx={{
                position: 'absolute',
                right: 8,
                top: 8,
                color: (theme) => theme.palette.grey[500],
            }}
          >
            <CloseIcon />
          </IconButton>
          <Typography id="modal-modal-title" variant="h6" component="h2" style={{color: 'black'}}>
          Login
          <Divider />
          </Typography>
          <form onSubmit={handleSubmit}>
              <TextField
                  label="Username"
                  value={usernameField}
                  onChange={handleUsernameChange}
                  margin="normal"
                  required
                  fullWidth
              />
              <TextField
                  label="Password"
                  type={showPassword ? "text" : "password"}
                  value={password}
                  InputProps={{
                    endAdornment: (
                      <InputAdornment position="end">
                        <IconButton
                          aria-label="toggle password visibility"
                          onClick={() => setShowPassword(!showPassword)}
                          edge="end"
                        >
                          {showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
                        </IconButton>
                      </InputAdornment>
                    ),
                  }}
                  onChange={handlePasswordChange}
                  margin="normal"
                  required
                  fullWidth
              />
              <br />
              {error && <Typography color="error">{error}</Typography>}
              <Button type="submit">Login</Button>
          </form>
          <Button onClick={openRegisterModal}>Register instead?</Button>
        </Box>
      </Fade>
    </Modal>
    </>
  );
}

export { LoginModal };