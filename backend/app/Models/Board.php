<?php
namespace App\Models;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;
class Board extends Model {
    protected $fillable = ['title'];
    public function lists(): HasMany { return $this->hasMany(BoardList::class)->orderBy('position'); }
    public function members(): BelongsToMany { return $this->belongsToMany(Member::class, 'board_member'); }
    public function tags(): HasMany { return $this->hasMany(Tag::class); }
}
