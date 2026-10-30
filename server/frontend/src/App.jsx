import React, {useEffect,useState} from 'react';
import Register from './components/Register/Register.jsx';
export default function App(){
 const [dealers,setDealers]=useState([]); const [user,setUser]=useState(null);
 useEffect(()=>{fetch('/api/dealers/').then(r=>r.json()).then(setDealers);fetch('/api/user/').then(r=>r.json()).then(d=>setUser(d.username));},[]);
 return <main><nav><a href="/">Home</a> <a href="/About.html">About Us</a> <a href="/Contact.html">Contact Us</a> <span>{user?'Signed in: '+user:'Guest'}</span></nav>
 <h1>Find a Dealership</h1><p>Browse dealerships and read customer reviews.</p>
 <section className="cards">{dealers.map(d=><article key={d.id}><h2>{d.full_name}</h2><p>{d.city}, {d.state}</p><a href={'/api/dealers/'+d.id+'/reviews/'}>View reviews</a></article>)}</section>
 <Register/><footer>Dealership Review Capstone</footer></main>;
}