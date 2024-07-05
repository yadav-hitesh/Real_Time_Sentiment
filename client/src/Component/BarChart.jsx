// BarChart.js
import React from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import Context from './Context';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const BarChart = () => {
    const {output} = React.useContext(Context);

    const data = {
        labels: ['Ambiguous', 'Mixed', 'Negative', 'Neutral', 'Positive'], // x-axis labels
        datasets: [
        {
            label: 'Tweets',
            data: [output.Ambiguous, output.Mixed, output.Negative, output.Neutral, output.Positive], // y-axis points
            backgroundColor: [
            'rgba(146, 96, 221, 0.2)',
            'rgba(84, 184, 243, 0.2)',
            'rgba(224, 101, 178, 0.2)',
            'rgba(250, 229, 97, 0.2)',
            'rgba(112, 241, 213, 0.2)',
            ],
            borderColor: [
            'rgba(146, 96, 221, 1)',
            'rgba(84, 184, 243, 1)',
            'rgba(224, 101, 178, 1)',
            'rgba(250, 229, 97, 1)',
            'rgba(112, 241, 213, 1)',
            ],
            borderWidth: 1,
        },
        ],
    };

    const options = {
        responsive: true,
        plugins: {
        legend: {
            position: 'top',
        },
        title: {
            display: true,
            text: 'Bar Chart Example',
        },
        },
        scales: {
        y: {
            beginAtZero: true,
            max: 20,
        },
        },
    };

    return <Bar data={data} options={options} />;
};

export default BarChart;
