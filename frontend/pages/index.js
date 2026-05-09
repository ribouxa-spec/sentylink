import Head from 'next/head';

export default function Home() {
  return (
    <div style={{ 
      backgroundColor: '#FDFBF7', 
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      fontFamily: 'Arial, sans-serif',
      color: '#2C3E50'
    }}>
      <Head>
        <title>Sentylink - Lien familial</title>
      </Head>

      <h1 style={{ color: '#5D9BEC', fontSize: '3rem' }}>🕊️ Sentylink</h1>
      <p style={{ fontSize: '1.2rem', color: '#34495E' }}>
        Lien familial & soutien mutuel
      </p>
      
      <div style={{ marginTop: '40px', textAlign: 'center', padding: '20px', backgroundColor: 'white', borderRadius: '10px', boxShadow: '0 2px 10px rgba(0,0,0,0.1)' }}>
        <p style={{ color: '#2C3E50' }}>
          ✅ Backend Python prêt
        </p>
        <p style={{ color: '#7F8C8D', fontSize: '0.9rem' }}>
          180 protocoles Sentinelles chargés
        </p>
      </div>
    </div>
  );
}