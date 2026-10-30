import React,{useState} from 'react';
export default function Register(){
 const [form,setForm]=useState({username:'',first_name:'',last_name:'',email:'',password:''});
 const [message,setMessage]=useState('');
 const change=e=>setForm({...form,[e.target.name]:e.target.value});
 async function submit(e){e.preventDefault();const r=await fetch('/api/register/',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(form)});const d=await r.json();setMessage(d.message||d.error||'Please check your details.');}
 return <section><h2>Sign-up</h2><form onSubmit={submit}>
 {['username','first_name','last_name','email','password'].map(k=><input key={k} name={k} placeholder={k.replace('_',' ').replace(/\b\w/g,c=>c.toUpperCase())} type={k==='password'?'password':k==='email'?'email':'text'} value={form[k]} onChange={change} required/>)}
 <button>Register</button></form><p>{message}</p></section>;
}