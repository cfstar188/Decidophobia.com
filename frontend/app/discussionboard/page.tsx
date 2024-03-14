import React, { useState } from 'react';

const App = () => {
  // Define state variables
  const [yourMessage, setYourMessage] = useState('');
  const [messagesList, setMessagesList] = useState([]);

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Add logic to handle form submission (e.g., sending data to server)
    // For now, just update messagesList with the new message
    setMessagesList([...messagesList, { user: { username: 'YourUsername' }, message: yourMessage }]);
    setYourMessage(''); // Clear input field after submission
  };

  return (
    <div className="divmain">
      <a href="http://127.0.0.1:8000/" style={{ textDecoration: 'none', color: '#fff', fontSize: '1vw' }}>Home</a>
      <br /><br /><br />
      <form onSubmit={handleSubmit}>
        <label style={{ color: '#fff', fontSize: '1.5vw' }} htmlFor="your_message">Your message:</label>
        <input style={{ fontSize: '1.5vw' }} id="your_message" type="text" value={yourMessage} onChange={(e) => setYourMessage(e.target.value)} />
        <input style={{ fontSize: '1.5vw' }} type="submit" value="OK" />
      </form>

      <table style={{ width: '100%' }}>
        <thead>
          <tr>
            <th style={{ color: '#fff', fontSize: '2vw' }}>Message Number</th>
            <th style={{ color: '#fff', fontSize: '2vw' }}>Author</th>
            <th style={{ color: '#fff', fontSize: '2vw' }}>Message</th>
          </tr>
        </thead>
        <tbody style={{ textAlign: 'center' }}>
          {messagesList.map((entry, index) => (
            <tr key={index}>
              <td style={{ color: '#fff', fontSize: '1.5vw' }}>{index + 1}</td>
              <td style={{ color: '#fff', fontSize: '1.5vw' }}>{entry.user.username}</td>
              <td style={{ color: '#fff', fontSize: '1.5vw' }}>{entry.message}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default App;
