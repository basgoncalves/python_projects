import React from 'react';

interface HeaderProps {
  userName?: string;
  date?: string;
  avatarUrl?: string;
  onButtonClick?: () => void;
}

const Header: React.FC<HeaderProps> = ({
  userName = "Linh",
  date = "Thursday, 08 July",
  avatarUrl = "https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/avatar.png",
  onButtonClick = () => console.log("Button clicked")
}) => {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0 16px',
      width: '100%',
      minWidth: '327px',
      height: '56px',
      boxSizing: 'border-box'
    }}>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: '16px'
      }}>
        <div style={{
          position: 'relative',
          width: '56px',
          height: '56px',
        }}>
          <img 
            src={avatarUrl} 
            alt="Avatar"
            style={{
              width: '100%',
              height: '100%',
              borderRadius: '50%',
              objectFit: 'cover'
            }}
          />
          <img 
            src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-8.png"
            alt="Icon"
            style={{
              position: 'absolute',
              bottom: '4px',
              right: '4px',
              width: '16px',
              height: '16px'
            }}
          />
        </div>

        <div style={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center'
        }}>
          <div style={{
            color: '#7f7f7f',
            fontSize: '14px',
            lineHeight: '24px',
            fontFamily: 'Circular Std',
            fontWeight: 400,
          }}>
            Hello {userName}!
          </div>
          <div style={{
            color: '#040415',
            fontSize: '18px',
            lineHeight: '28px',
            fontFamily: 'Circular Std',
            fontWeight: 700,
          }}>
            {date}
          </div>
        </div>
      </div>

      <button 
        onClick={onButtonClick}
        style={{
          width: '56px',
          height: '56px',
          border: 'none',
          background: 'transparent',
          cursor: 'pointer',
          padding: 0
        }}
      >
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/button.png" 
          alt="Menu"
          style={{
            width: '100%',
            height: '100%'
          }}
        />
      </button>
    </div>
  );
};

export default Header;

