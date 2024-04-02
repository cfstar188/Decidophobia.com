import { useAtom } from 'jotai';
import React, { useState } from 'react';
import { useRouter } from 'next/navigation' // corrected from 'next/navigation'
import { Button, Box, Modal, TextField, Typography, Divider } from '@mui/material';
import * as Yup from 'yup';
import { set, useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import { IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import Fade from '@mui/material/Fade';
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import InputAdornment from '@mui/material/InputAdornment';

import axios from 'axios';

interface RegisterModalProps {
    isOpen: boolean;
    onClose: () => void;
    setIsLoginModalOpen: (value: boolean) => void;
}

export default function RegisterModal({ isOpen, onClose, setIsLoginModalOpen }: RegisterModalProps) {
  const router = useRouter()
  const validationSchema = Yup.object().shape({
    username: Yup.string()
    .min(5, 'Username must be at least 5 characters long')
    .max(15, 'Username must be less than 15 characters long')
    .required('Username is required'),
    password: Yup.string()
    .min(8, 'Password must be at least 8 characters long')
    .matches(/^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$/, 'Password must contain at least one uppercase letter, one lowercase letter, and one number')
    .required('Password is required'),
    password2: Yup.string()
    .oneOf([Yup.ref('password'), ''], 'Passwords must match')
    .required('Confirm Password is required'),
    email: Yup.string()
    .email('Email is invalid')
    .required('Email is required')
  });
  
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [image, setImage] = useState<File | null>(null);
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

  const { register, handleSubmit, formState: { errors }, reset } = useForm({mode: 'onChange',
    resolver: yupResolver(validationSchema)
  });

  const resetImage = () => {
    setImage(null);
    const fileInput = document.getElementById('contained-button-file') as HTMLInputElement;
    if (fileInput) {
      fileInput.value = '';
    }
  };

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
        setImage(event.target.files[0]);
    }
  };

  const onSubmit = (data: any) => {
    const formData = new FormData();
    formData.append('username', data.username);
    formData.append('password', data.password);
    formData.append('password2', data.password2);
    formData.append('email', data.email);
    if (image) {
      formData.append('profile_picture', image);
    }

    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
    axios.defaults.withCredentials = true;
    const api = axios.create();

    api.post('http://127.0.0.1:8000/accounts/register/', formData, {
      headers: {"Content-Type": "multipart/form-data"},
    })
    .then((response: any) => {
      openLoginModal();
    })
    .catch((error: any) => {
        const errorJSON = JSON.parse(error.request.response);
        setError(errorJSON.non_field_errors[0]);
    });
  }

  const openLoginModal = () => {
    handleClose();
    setIsLoginModalOpen(true);
  }

  const handleClose = () => {
    setImage(null);
    setError('');
    reset();
    onClose();
  }

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
                Register
                <Divider />
                </Typography>
                <form onSubmit={handleSubmit(onSubmit)}>
                    <TextField
                        label="Username"
                        {...register('username')}
                        error={errors.username ? true : false}
                        helperText={errors.username ? errors.username.message : ''}
                        margin="normal"
                        required
                        fullWidth
                    />
                    <TextField
                        label="Password"
                        type={showPassword ? "text" : "password"}
                        {...register('password')}
                        error={errors.password ? true : false}
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
                        helperText={errors.password ? errors.password.message : ''}
                        margin="normal"
                        required
                        fullWidth
                    />
                    <TextField
                        label="Confirm Password"
                        type={showPassword ? "text" : "password"}
                        {...register('password2')}
                        error={errors.password2 ? true : false}
                        helperText={errors.password2 ? errors.password2.message : ''}
                        margin="normal"
                        required
                        fullWidth
                    />
                    <TextField
                        label="Email"
                        type="email"
                        {...register('email')}
                        error={errors.email ? true : false}
                        helperText={errors.email ? errors.email.message : ''}
                        margin="normal"
                        fullWidth
                    />
                    <div style={{ display: 'flex', alignItems: 'center' }}>
                      <img
                        src={image ? URL.createObjectURL(image) : '/default.jpg'}
                        alt="profile"
                        style={{objectFit:"contain", width: '5rem', height: '5rem'}}
                      />
                      <p style={{ 
                        fontSize: '1rem', 
                        marginLeft: '10px', 
                        color: 'darkgray', 
                        alignSelf: 'flex-end',
                        textOverflow: 'ellipsis',
                        overflow: 'hidden',
                        whiteSpace: 'nowrap'
                      }}>{image ? image.name : ''}</p>
                    </div>
                    <input
                      accept="image/*"
                      type="file"
                      id="contained-button-file"
                      onChange={handleFileChange}
                      hidden
                    />
                    <div
                      style={{marginTop: '10px'}}>
                      <label htmlFor="contained-button-file">
                        <Button variant="contained" component="span">
                            Upload Image
                        </Button>
                      </label>
                      <label style={{ marginLeft: '10px' }}>
                        <Button variant="contained" component="span" onClick={resetImage}>
                            Reset Image
                        </Button>
                      </label>
                    </div>
                    <br />
                    {error && <Typography color="error">{error}</Typography>}
                    <Button type="submit">Register</Button>
                </form>
                <Button onClick={openLoginModal}>Login instead?</Button>
            </Box>
        </Fade>
    </Modal>
    </>
  );
}

export { RegisterModal }