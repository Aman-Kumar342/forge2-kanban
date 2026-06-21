<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
class Card extends Model {
    protected $fillable = ['list_id', 'title', 'description', 'position', 'assignee_id', 'due_date'];
    protected $casts = ['due_date' => 'date'];
    public function list(): BelongsTo { return $this->belongsTo(BoardList::class, 'list_id'); }
    public function assignee(): BelongsTo { return $this->belongsTo(Member::class, 'assignee_id'); }
    public function tags(): BelongsToMany { return $this->belongsToMany(Tag::class, 'card_tag'); }
}
