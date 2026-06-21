<?php
namespace App\Http\Controllers\Api;
use App\Http\Controllers\Controller;
use App\Models\Board;
use App\Models\BoardList;
use App\Models\Card;
use App\Models\Member;
use App\Models\Tag;
use Illuminate\Http\Request;
class KanbanController extends Controller {
    public function boards() { return Board::with(['lists.cards.assignee','lists.cards.tags','members','tags'])->get(); }
    public function createBoard(Request $r) {
        $data = $r->validate(['title'=>'required|string|max:255']);
        $board = Board::create($data);
        foreach (['To Do','Doing','Done'] as $i=>$t) BoardList::create(['board_id'=>$board->id,'title'=>$t,'position'=>$i]);
        return $board->load(['lists.cards','members','tags']);
    }
    public function createList(Request $r, Board $board) {
        $data = $r->validate(['title'=>'required|string|max:255']);
        return BoardList::create(['board_id'=>$board->id,'title'=>$data['title'],'position'=>$board->lists()->max('position')+1]);
    }
    public function createCard(Request $r, BoardList $list) {
        $data = $r->validate(['title'=>'required|string|max:255','description'=>'nullable|string','due_date'=>'nullable|date','assignee_id'=>'nullable|exists:members,id']);
        return Card::create([...$data,'list_id'=>$list->id,'position'=>$list->cards()->max('position')+1])->load(['assignee','tags']);
    }
    public function updateCard(Request $r, Card $card) {
        $data = $r->validate(['title'=>'sometimes|string|max:255','description'=>'nullable|string','due_date'=>'nullable|date','assignee_id'=>'nullable|exists:members,id','list_id'=>'sometimes|exists:lists,id','position'=>'sometimes|integer']);
        $card->update($data); return $card->fresh(['assignee','tags']);
    }
    public function moveCard(Request $r, Card $card) {
        $data = $r->validate(['list_id'=>'required|exists:lists,id','position'=>'integer']);
        $card->update($data); return $card->fresh(['assignee','tags']);
    }
    public function addMember(Request $r, Board $board) {
        $data = $r->validate(['name'=>'required|string|max:255','email'=>'nullable|email']);
        $m = Member::create($data); $board->members()->attach($m->id); return $m;
    }
    public function createTag(Request $r, Board $board) {
        $data = $r->validate(['name'=>'required|string|max:50','color'=>'nullable|string|max:20']);
        return Tag::create(['board_id'=>$board->id,'name'=>$data['name'],'color'=>$data['color']??'#6366f1']);
    }
    public function attachTag(Card $card, Tag $tag) { $card->tags()->syncWithoutDetaching([$tag->id]); return $card->fresh(['tags','assignee']); }
    public function detachTag(Card $card, Tag $tag) { $card->tags()->detach($tag->id); return $card->fresh(['tags','assignee']); }
}
