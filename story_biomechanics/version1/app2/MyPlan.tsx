import React from 'react';

interface MyPlanProps {
  date?: string;
  week?: string;
  workoutProgress?: string;
  nextExercise?: string;
}

const MyPlan: React.FC<MyPlanProps> = ({
  date = "July, 2021",
  week = "WEEK 1",
  workoutProgress = "Workout 1 of 5",
  nextExercise = "Lower Strength"
}) => {
  return (
    <div style={{
      width: '100%',
      maxWidth: '327px',
      padding: '0',
      display: 'flex',
      flexDirection: 'column',
      gap: '24px',
      margin: '0 auto'
    }}>
      {/* Title Section */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        width: '100%',
        height: '56px'
      }}>
        <div style={{
          display: 'flex',
          flexDirection: 'column',
          gap: '4px'
        }}>
          <h2 style={{
            margin: '0',
            fontSize: '18px',
            fontWeight: 700,
            lineHeight: '28px',
            color: '#040415'
          }}>My Plan</h2>
          <span style={{
            fontSize: '14px',
            fontWeight: 400,
            lineHeight: '24px',
            color: '#7F7F7F'
          }}>{date}</span>
        </div>
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-7.png"
          alt="settings"
          style={{
            width: '24px',
            height: '24px',
            cursor: 'pointer'
          }}
        />
      </div>

      {/* Card Section */}
      <div style={{
        width: '100%',
        height: '198px',
        background: '#FFFFFF',
        borderRadius: '16px',
        padding: '28px 24px',
        boxSizing: 'border-box',
        display: 'flex',
        flexDirection: 'column',
        gap: '30px',
        position: 'relative',
        overflow: 'hidden'
      }}>
        {/* Background Image */}
        <img 
          src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/base-5.png"
          alt="background"
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            zIndex: 0
          }}
        />

        {/* Top Content */}
        <div style={{
          display: 'flex',
          gap: '24px',
          zIndex: 1
        }}>
          <img 
            src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-6.png"
            alt="workout"
            style={{
              width: '56px',
              height: '56px'
            }}
          />
          <div style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '2px'
          }}>
            <span style={{
              fontSize: '12px',
              fontWeight: 400,
              lineHeight: '16px',
              color: '#7F7F7F'
            }}>{week}</span>
            <h3 style={{
              margin: '0',
              fontSize: '18px',
              fontWeight: 700,
              lineHeight: '28px',
              color: '#040415'
            }}>Body Weight</h3>
            <span style={{
              fontSize: '12px',
              fontWeight: 400,
              lineHeight: '16px',
              color: '#040415'
            }}>{workoutProgress}</span>
          </div>
        </div>

        {/* Next Exercise Section */}
        <div style={{
          display: 'flex',
          gap: '16px',
          alignItems: 'center',
          background: '#FFFFFF',
          borderRadius: '16px',
          padding: '12px',
          zIndex: 1
        }}>
          <img 
            src="https://dashboard.codeparrot.ai/api/image/Z8YA_chTinWyM7G5/icon-5.png"
            alt="next"
            style={{
              width: '24px',
              height: '24px'
            }}
          />
          <div style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '0px'
          }}>
            <span style={{
              fontSize: '12px',
              fontWeight: 400,
              lineHeight: '16px',
              color: '#7F7F7F'
            }}>Next exercise</span>
            <span style={{
              fontSize: '14px',
              fontWeight: 700,
              lineHeight: '24px',
              color: '#040415'
            }}>{nextExercise}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default MyPlan;

