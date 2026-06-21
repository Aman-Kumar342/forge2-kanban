<?php
use App\Http\Controllers\Api\KanbanController;
use Illuminate\Support\Facades\Route;
Route::get('/boards', [KanbanController::class, 'boards']);
Route::post('/boards', [KanbanController::class, 'createBoard']);
Route::post('/boards/{board}/lists', [KanbanController::class, 'createList']);
Route::post('/boards/{board}/members', [KanbanController::class, 'addMember']);
Route::post('/boards/{board}/tags', [KanbanController::class, 'createTag']);
Route::post('/lists/{list}/cards', [KanbanController::class, 'createCard']);
Route::patch('/cards/{card}', [KanbanController::class, 'updateCard']);
Route::post('/cards/{card}/move', [KanbanController::class, 'moveCard']);
Route::post('/cards/{card}/tags/{tag}', [KanbanController::class, 'attachTag']);
Route::delete('/cards/{card}/tags/{tag}', [KanbanController::class, 'detachTag']);
