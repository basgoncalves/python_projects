import React from 'react';

interface AppbarProps {
  onHomeClick?: () => void;
  onLocationClick?: () => void;
  onAddClick?: () => void;
  onHeartClick?: () => void;
  onMedalClick?: () => void;
}

const Appbar: React.FC<AppbarProps> = ({
  onHomeClick = () => {},
  onLocationClick = () => {},
  onAddClick = () => {},
  onHeartClick = () => {},
  onMedalClick = () => {}
}) => {
  return (
    <div style={{
      width: '100%',
      maxWidth: '375px',
      height: '105px',
      backgroundColor: '#ffffff',
      borderRadius: '40px',
      display: 'flex',
      justifyContent: 'space-around',
      alignItems: 'center',
      padding: '0 15px',
      boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.1)',
      position: 'fixed',
      bottom: '0',
      left: '50%',
      transform: 'translateX(-50%)'
    }}>
      <div 
        onClick={onHomeClick}
        style={{
          width: '60px',
          height: '105px',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: 'pointer'
        }}
      >
        <span style={{
          fontFamily: 'Circular Std',
          fontWeight: 700,
          fontSize: '14px',
          lineHeight: '24px',
          color: '#040415',
          textAlign: 'center'
        }}>
          Home
        </span>
        <div style={{
          width: '4px',
          height: '4px',
          backgroundColor: '#f15223',
          borderRadius: '50%',
          marginTop: '4px'
        }} />
      </div>

      <div 
        onClick={onLocationClick}
        style={{
          width: '60px',
          height: '105px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: 'pointer'
        }}
      >
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icons-3.png"
          alt="location"
          style={{
            width: '24px',
            height: '24px'
          }}
        />
      </div>

      <div 
        onClick={onAddClick}
        style={{
          width: '65px',
          height: '65px',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: 'linear-gradient(135deg, #f15223, #f15223)',
          borderRadius: '50%',
          boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.1)'
        }}
      >
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/⚙️-item-3.png"
          alt="add"
          style={{
            width: '24px',
            height: '24px'
          }}
        />
      </div>

      <div 
        onClick={onHeartClick}
        style={{
          width: '60px',
          height: '105px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: 'pointer'
        }}
      >
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icons-2.png"
          alt="heart"
          style={{
            width: '24px',
            height: '24px'
          }}
        />
      </div>

      <div 
        onClick={onMedalClick}
        style={{
          width: '60px',
          height: '105px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          cursor: 'pointer'
        }}
      >
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icons.png"
          alt="medal"
          style={{
            width: '24px',
            height: '24px'
          }}
        />
      </div>
    </div>
  );
};

export default Appbar;

