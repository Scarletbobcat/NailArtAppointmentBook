import Navbar from "./Navbar"
import Home from "./pages/Home"
import Create from "./pages/Create";
import Delete from "./pages/Delete";
import NailTechs from "./pages/NailTechs";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className="App">
        < Navbar />
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/create-appointment" element={<Create/>}></Route>
          <Route path="/delete-appointment" element={<Delete/>}></Route>
          <Route path="/nail-techs" element={<NailTechs/>}></Route>
        </Routes>
      </div>
    </Router>
  );
}

export default App;