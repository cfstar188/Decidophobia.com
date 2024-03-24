import { useState } from 'react';
import Button from '@mui/material/Button';
import Snackbar from '@mui/material/Snackbar';
import Alert from '@mui/material/Alert';
type AlertsProps = {
    message: string;
    severity: 'error' | 'warning' | 'info' | 'success';
    isOpen: boolean;
    onClose: () => void;
};

const Alerts: React.FC<AlertsProps> = ({ message, severity, isOpen, onClose }) => {

  return (
    <Snackbar anchorOrigin={{vertical:'bottom', horizontal:'right'}} open={isOpen} autoHideDuration={3000} onClose={onClose}>
      <Alert onClose={onClose} severity={severity} variant='filled' sx={{ width: '100%' }}>
        {message}
      </Alert>
    </Snackbar>
  );
}

export default Alerts;