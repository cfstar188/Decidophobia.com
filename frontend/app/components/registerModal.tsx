import { useAtom } from 'jotai';
import React, { useState } from 'react';
import { useRouter } from 'next/navigation' // corrected from 'next/navigation'
import { Button, Box, Modal, TextField, Typography, Divider } from '@mui/material';
import * as Yup from 'yup';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import { IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import Fade from '@mui/material/Fade';

import { authAtom } from '@/Library/AuthAtom';
import api from '../core/baseAPI';
import { on } from 'events';

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
      .required('Password is required'),
    password2: Yup.string()
      .oneOf([Yup.ref('password'), ''], 'Passwords must match')
      .required('Confirm Password is required'),
    email: Yup.string()
      .email('Email is not valid')
  });

  const [error, setError] = useState('');
  const [auth, setAuth] = useAtom(authAtom);
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

  const onSubmit = (data: any) => {
    api.post('accounts/register/', {
      username: data.username,
      password: data.password,
      password2: data.password2,
      email: data.email
    }, {
      headers: {"Content-Type": "application/json"},
    })
    .then((response: any) => {
      localStorage.setItem('token', JSON.stringify(response.data));
      setAuth({ isAuthenticated: true, username: data.username });
      handleClose();
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
                        type="password"
                        {...register('password')}
                        error={errors.password ? true : false}
                        helperText={errors.password ? errors.password.message : ''}
                        margin="normal"
                        required
                        fullWidth
                    />
                    <TextField
                        label="Confirm Password"
                        type="password"
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

export { RegisterModal };