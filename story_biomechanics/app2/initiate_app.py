import os

# Define the directory structure and file contents
project_structure = {
    "app2": {
        "RecentPlan.tsx": """import React from 'react';

interface PlanItem {
  icon: string;
  title: string;
  background: string;
}

const RecentPlan: React.FC = () => {
  const planItems: PlanItem[] = [
    {
      icon: 'https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon.png',
      title: 'Special',
      background: 'linear-gradient(133.34deg, rgba(253,55,31,1) 34.27%, rgba(255,132,75,1) 99.34%)',
    },
    {
      icon: 'https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-2.png',
      title: 'Beach Rea…',
      background: 'linear-gradient(135deg, rgba(101,207,88,1) 0%, rgba(101,207,88,0.6) 99.35%)',
    },
    {
      icon: 'https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-3.png',
      title: 'Full - Body',
      background: 'linear-gradient(135deg, rgba(255,180,50,1) 0%, rgba(255,180,50,0.6) 93.03%)',
    },
    {
      icon: 'https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-4.png',
      title: 'Challenged',
      background: 'linear-gradient(135deg, rgba(105,224,199,1) 0%, rgba(105,224,199,0.6) 94.69%)',
    },
  ];

  return (
    <div style={{
      width: '100%',
      maxWidth: '368px',
      padding: '20px',
      fontFamily: 'Circular Std, sans-serif',
    }}>
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: '24px',
      }}>
        <div>
          <h2 style={{
            margin: '0',
            fontSize: '18px',
            fontWeight: 700,
            lineHeight: '28px',
            color: '#040415',
          }}>
            Recent Plan
          </h2>
          <p style={{
            margin: '4px 0 0 0',
            fontSize: '14px',
            fontWeight: 400,
            lineHeight: '24px',
            color: '#7f7f7f',
          }}>
            July, 2021
          </p>
        </div>
        <button style={{
          background: 'none',
          border: 'none',
          padding: 0,
          fontSize: '14px',
          fontWeight: 700,
          lineHeight: '24px',
          color: '#f15223',
          cursor: 'pointer',
        }}>
          See All
        </button>
      </div>

      <div style={{
        display: 'flex',
        gap: '16px',
        overflowX: 'auto',
      }}>
        {planItems.map((item, index) => (
          <div key={index} style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            width: '80px',
            flexShrink: 0,
          }}>
            <div style={{
              width: '64px',
              height: '64px',
              borderRadius: '24px',
              background: item.background,
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center',
              marginBottom: '14px',
              cursor: 'pointer',
            }}>
              <img 
                src={item.icon} 
                alt={item.title}
                style={{
                  width: '36px',
                  height: '36px',
                }}
              />
            </div>
            <span style={{
              fontSize: '14px',
              fontWeight: 700,
              lineHeight: '24px',
              color: '#040415',
              textAlign: 'center',
              width: '100%',
            }}>
              {item.title}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecentPlan;
"""
    },
    "src": {
        "index.js": """import React from 'react';
import ReactDOM from 'react-dom';
import RecentPlan from '../app2/RecentPlan';

ReactDOM.render(<RecentPlan />, document.getElementById('root'));
""",
        "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My React App</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
"""
    },
    ".babelrc": """{
  "presets": ["@babel/preset-env", "@babel/preset-react"]
}
""",
    "webpack.config.js": """const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
  ],
  devServer: {
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 9000,
  },
};
""",
    "tsconfig.json": """{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "strict": true,
    "jsx": "react",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
"""
}

# Function to create the directory structure and files
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)

# Create the project structure
base_path = "C:/Git/python_projects/story_biomechanics"
create_project_structure(base_path, project_structure)