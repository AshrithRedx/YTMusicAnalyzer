import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import './App.css';

function App() {
  const [playlistId, setPlaylistId] = useState('');
  const [data, setData] = useState(null);

  const fetchStats = async () => {
    try {
      const res = await axios.get(`https://ytmusicanalyzer.onrender.com/analyze?playlist_id=${playlistId}`);
      setData(res.data);
    } catch (err) {
      console.error(err);
      alert("Error fetching stats. Check playlist ID or server.");
    }
  };

  return (
    <div className="app">
      <h1>🎶 YTMusic Playlist Analyzer</h1>
      <input
        type="text"
        placeholder="Enter YouTube Music Playlist ID"
        value={playlistId}
        onChange={(e) => setPlaylistId(e.target.value)}
      />
      <button onClick={fetchStats}>Get Stats</button>

      {data && (
        <div className="results">
          <h2>🎧 {data.playlist_title}</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data.artist_data}>
              <XAxis dataKey="Artist" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="Song Count" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>

          <div className="cards">
            {data.artist_data.map((artist, idx) => (
              <div key={idx} className="card">
                <h3>{artist.Artist}</h3>
                <p>🎶 {artist["Song Count"]} songs</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
