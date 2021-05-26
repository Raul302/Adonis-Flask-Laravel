<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\note;

class NotesController extends Controller
{
    //
    public function show(Request $request){
        $notes = note::all();
        return response()->json($notes,200);
    }

    public function save(Request $request){
        $note = note::create($request->all());
        return response()->json($note,200);

    }
}
