'use strict'

const Notes = use('App/Models/Note');
class NoteController {

    async save ({request}){
    const dataToCreate = request.only(['name', 'description']);
	return await Notes.create(dataToCreate);
    }

    async display ({request}){
        return await Notes.all();
        }
}

module.exports = NoteController
