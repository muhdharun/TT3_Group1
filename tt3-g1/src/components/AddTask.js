// import React from 'react';
import { useState } from 'react'

const AddTask = ({onAdd}) => {
    const [datetime, setDatetime] = useState('')
    const [caption, setCaption] = useState('')
    const [hashtags, setHashtags] = useState('')
    // const [reminder, setReminder] = useState(false)

    const onSubmit = (e) => {
        e.preventDefault()

        if(!caption) {
            alert('Please add a caption')
            return
        }

        onAdd({ datetime, caption, hashtags})

        setDatetime('')
        setCaption('')
        setHashtags('')

    }

  return <form className='add-form' onSubmit={onSubmit}>
      <div className='form-control'>
          <label>DateTime</label>
          <input type='text' 
          placeholder='Add Date & Time' 
          value={datetime} 
          onChange={(e) => setDatetime(e.target.value)} />
      </div>
      <div className='form-control'>
          <label>Caption</label>
          <input type='text' 
          placeholder='Add Caption' 
          value={caption} 
          onChange={(e) => setCaption(e.target.value)} />
      </div>
      <div className='form-control'>
          <label>Hashtags</label>
          <input type='text' 
          placeholder='Add Hashtags'
          value={hashtags} 
          onChange={(e) => setHashtags(e.target.value)} />
      </div>

      <input 
      type='submit' 
      // checked={reminder}
      value='Submit Post' 
      className='btn btn-block' />
  </form>
};

export default AddTask;
