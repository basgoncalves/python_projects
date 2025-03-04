import React from 'react';
import Header from './Header';
import MyPlan from './MyPlan';
import RecentPlan from './RecentPlan';
import Appbar from './Appbar';

const Layout: React.FC = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', width: '100%', minHeight: '100vh', alignItems: 'center', backgroundColor: '#f8f8f8' }}>
      <div style={{ flexGrow: 0, flexShrink: 0, width: '100%', maxWidth: '375px' }}>
        <Header />
      </div>
      <div style={{ flexGrow: 1, flexShrink: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', width: '100%', maxWidth: '375px', padding: '16px 0' }}>
        <MyPlan />
        <RecentPlan />
      </div>
      <div style={{ flexGrow: 0, flexShrink: 0, width: '100%', maxWidth: '375px' }}>
        <Appbar />
      </div>
    </div>
  );
};

export default Layout;

