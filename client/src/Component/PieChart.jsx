import * as React from 'react';

import { PieChart, pieArcLabelClasses } from '@mui/x-charts/PieChart';
import Context from './Context';

const PieChartData = () => {

    const {output} = React.useContext(Context);

    const data = [
            { label: 'Ambigious', value: output.Ambiguous, color: '#9b5de5' },
            { label: 'Mixed', value: output.Mixed, color: '#00bbf9' },
            { label: 'Negative', value: output.Negative, color: '#f15bb5' },
            { label: 'Neutral', value: output.Neutral, color: '#fee440' },
            { label: 'Positive', value: output.Positive, color: '#00f5d4' },
        ];
        
        const sizing = {
            margin: { right: 5 },
            width: 600,
            height: 300,
            // legend: { hidden: true },
        };
        const TOTAL = data.map((item) => item.value).reduce((a, b) => a + b, 0);
        
        const getArcLabel = (params) => {
            const percent = params.value / TOTAL;
            return `${(percent * 100).toFixed(0)}%`;
        };

    return (
        <PieChart
        series={[
            {
                innerRadius: 40,
                outerRadius: 120,
                data,
                arcLabel: getArcLabel,
            },
        ]}
        sx={{
            [`& .${pieArcLabelClasses.root}`]: {
            fill: 'white',
            fontSize: 14,
            },
        }}
        {...sizing}
        />
    );
}

export default PieChartData