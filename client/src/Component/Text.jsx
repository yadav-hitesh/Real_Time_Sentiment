import {React, useContext, useState} from 'react';
import axios from 'axios';
import Context from './Context';
import PieChartData from './PieChart';
import BarChart from './BarChart';
import ClipLoader from 'react-spinners/ClipLoader';


const Text = () => {
    const [text, setText] = useState('');
    const [result, setResult] = useState(null);
    const [loading,setLoading] = useState(false);

    const {setOutput,output} = useContext(Context);
  
    const handleSubmit = async (e) => {
      // e.preventDefault();
      if (!text) return;
      
      setLoading(true);
  
      try {
        const response = await axios.post('http://127.0.0.1:5000/analyze', { text });
        // const response = await fetch('/analyze', {
        //   method: 'POST',
        //   body: {text}
        // });
        console.log(typeof(response.data));
        console.log(response.data);
        setResult(response.data);
        setOutput(response.data);
        console.log(result);
      } catch (error) {
        console.error('Error analyzing text', error);
      } finally{
        setLoading(false);
      }
    };
  
    const handleKey = (event) => {
      if(event.key === 'Enter')
      {
        handleSubmit();
      }
    }
  
    return (
      <div className="pt-0 p-10 ">
        <div className='mt-3'>
          <h className="border-2 rounded-lg h-20 mt-6 p-2 italic" style={{ background:'linear-gradient(#1f4e96,#fdf251)'}}>
            "Stay updated with the latest trends and public opinions on Twitter! Our sentiment analysis reveals real-time insights into how people feel about current topics and events."
          </h>
        </div>
        <h1 className='text-2xl mt-2'>Real-Time Sentiment Analysis</h1>
        <div>
          <textarea className='w-full m-5 border-2 rounded-md shadow-lg'
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={handleKey}
            placeholder="Enter text or HashTag to analyze"
            rows="4"
            cols="50"
          />
          <br />
          <button 
          className='border-2 h-10 px-4 text-white rounded-lg bg-[#1f4e96]'
          onClick={handleSubmit}>Analyze Sentiment</button>
        </div>
        <div>
          {loading && 
          (<div className="loader-container mt-4">
            <ClipLoader color="#36d7b7" loading={true} size={50} />
          </div>)}
            {result && (
              <div>
                {/* <h2 className='mt-10'>Sentiment Analysis Result</h2> */}
                <div className='flex w-full mr-10'>
                  <div className="mr-4 border-2 shadow-lg rounded-full mt-10 pt-0 p-5 w-1/2 h-80">
                      {/* <div className='text-right'>
                        
                      </div> */}
                      {/* {result.Positive} */}
                      <div className="mr-[30px]">
                        <PieChartData />
                      </div>
                  </div> 
                  <div className="ml-4 border-2 shadow-lg rounded-full px-16 mt-10 p-5 w-1/2">
                        {/* <p>Ambiguous: {result.Ambiguous}</p>
                        <p>Mixed: {result.Mixed}</p>
                        <p>Negative: {result.Negative}</p>
                        <p>Neutral: {result.Neutral}</p>
                        <p>Positive: {result.Positive}</p> */}
                        <BarChart/>
                  </div>
                </div>  
              </div>           
            )}
        </div>
      </div>
    );
}

export default Text