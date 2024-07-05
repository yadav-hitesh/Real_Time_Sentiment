import React, { createContext, useState} from 'react';

// Create a context 
const Context = createContext();

export const ContextProvider = ({ children }) => {

    const [output,setOutput] = useState();
    // {'Ambiguous':0,'Mixed':0,'Negative':0,'Neutral':0,'Positive':0}

    return (
        <Context.Provider value={{output,setOutput}}>
        {children}
        </Context.Provider>
    );
};

export default Context;