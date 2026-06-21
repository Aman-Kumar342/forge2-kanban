import { useEffect, useState } from 'react'
import './App.css'

const API = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api'

type Member = { id: number; name: string; email?: string }
type Tag = { id: number; name: string; color: string }
type Card = { id: number; title: string; description?: string; due_date?: string; assignee?: Member; tags?: Tag[]; list_id: number; position: number }
type List = { id: number; title: string; cards: Card[] }
type Board = { id: number; title: string; lists: List[]; members: Member[]; tags: Tag[] }

async function api(path: string, opts?: RequestInit) {
  const r = await fetch(`${API}${path}`, { headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, ...opts })
  if (!r.ok) throw new Error(await r.text())
  return r.json()
}

function isOverdue(d?: string) {
  if (!d) return false
  return new Date(d) < new Date(new Date().toDateString())
}

export default function App() {
  const [boards, setBoards] = useState<Board[]>([])
  const [board, setBoard] = useState<Board | null>(null)
  const [title, setTitle] = useState('Forge2 Kanban')

  const load = async () => {
    const data = await api('/boards')
    setBoards(data)
    if (data[0]) setBoard(data[0])
  }

  useEffect(() => { load().catch(console.error) }, [])

  const createBoard = async () => {
    const b = await api('/boards', { method: 'POST', body: JSON.stringify({ title }) })
    const data = await api('/boards')
    setBoards(data)
    setBoard(data.find((x: Board) => x.id === b.id) ?? null)
  }

  const addCard = async (listId: number) => {
    const t = prompt('Card title?')
    if (!t || !board) return
    await api(`/lists/${listId}/cards`, { method: 'POST', body: JSON.stringify({ title: t }) })
    await load()
    setBoard((await api('/boards')).find((b: Board) => b.id === board.id) || null)
  }

  const moveCard = async (card: Card, listId: number) => {
    await api(`/cards/${card.id}/move`, { method: 'POST', body: JSON.stringify({ list_id: listId, position: 0 }) })
    await load()
    if (board) setBoard((await api('/boards')).find((b: Board) => b.id === board.id) || null)
  }

  const editCard = async (card: Card) => {
    const desc = prompt('Description', card.description || '') ?? card.description
    const due = prompt('Due date YYYY-MM-DD (empty=none)', card.due_date?.slice(0,10) || '') || null
    await api(`/cards/${card.id}`, { method: 'PATCH', body: JSON.stringify({ description: desc, due_date: due }) })
    await load()
    if (board) setBoard((await api('/boards')).find((b: Board) => b.id === board.id) || null)
  }

  const addMember = async () => {
    if (!board) return
    const name = prompt('Member name?')
    if (!name) return
    await api(`/boards/${board.id}/members`, { method: 'POST', body: JSON.stringify({ name }) })
    await load()
    setBoard((await api('/boards')).find((b: Board) => b.id === board!.id) || null)
  }

  const assignMember = async (card: Card) => {
    if (!board) return
    const id = prompt(`Assign member id: ${board.members.map(m=>`${m.id}=${m.name}`).join(', ')}`)
    if (!id) return
    await api(`/cards/${card.id}`, { method: 'PATCH', body: JSON.stringify({ assignee_id: Number(id) }) })
    await load()
    setBoard((await api('/boards')).find((b: Board) => b.id === board!.id) || null)
  }

  const addTag = async () => {
    if (!board) return
    const name = prompt('Tag name?')
    if (!name) return
    const color = prompt('Color hex', '#6366f1') || '#6366f1'
    await api(`/boards/${board.id}/tags`, { method: 'POST', body: JSON.stringify({ name, color }) })
    await load()
    setBoard((await api('/boards')).find((b: Board) => b.id === board!.id) || null)
  }

  const tagCard = async (card: Card) => {
    if (!board) return
    const id = prompt(`Tag id: ${board.tags.map(t=>`${t.id}=${t.name}`).join(', ')}`)
    if (!id) return
    await api(`/cards/${card.id}/tags/${id}`, { method: 'POST' })
    await load()
    setBoard((await api('/boards')).find((b: Board) => b.id === board!.id) || null)
  }

  return (
    <div className="app">
      <header>
        <h1>Forge2 Kanban</h1>
        <div className="toolbar">
          <input value={title} onChange={e=>setTitle(e.target.value)} placeholder="Board title" />
          <button onClick={createBoard}>New Board</button>
          {board && <>
            <button onClick={addMember}>Add Member</button>
            <button onClick={addTag}>Add Tag</button>
            <select value={board.id} onChange={e=>setBoard(boards.find(b=>b.id===Number(e.target.value))||null)}>
              {boards.map(b=><option key={b.id} value={b.id}>{b.title}</option>)}
            </select>
          </>}
        </div>
      </header>
      {board && (
        <div className="board">
          {board.lists.map(list => (
            <div key={list.id} className="list">
              <h3>{list.title}</h3>
              {(list.cards ?? []).map(card => (
                <div key={card.id} className={`card ${isOverdue(card.due_date)?'overdue':''}`}>
                  <strong>{card.title}</strong>
                  {card.description && <p>{card.description}</p>}
                  {card.due_date && <small>Due: {card.due_date.slice(0,10)}</small>}
                  {card.assignee && <small>👤 {card.assignee.name}</small>}
                  <div className="tags">{card.tags?.map(t=><span key={t.id} style={{background:t.color}}>{t.name}</span>)}</div>
                  <div className="actions">
                    <button onClick={()=>editCard(card)}>Edit</button>
                    <button onClick={()=>assignMember(card)}>Assign</button>
                    <button onClick={()=>tagCard(card)}>Tag</button>
                    {board.lists.filter(l=>l.id!==list.id).map(l=>(
                      <button key={l.id} onClick={()=>moveCard(card,l.id)}>→ {l.title}</button>
                    ))}
                  </div>
                </div>
              ))}
              <button className="add" onClick={()=>addCard(list.id)}>+ Card</button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
