import React, { useState } from 'react';
import './App.css';
import Text from './Component/Text';
import { ContextProvider } from './Component/Context';
import Navbar from './Component/Navbar';

const App = () => {

  return (
    <ContextProvider>
      <div className="text-center">
        <Navbar/>
        <Text/>
      </div>
    </ContextProvider>
  );
};

export default App;
